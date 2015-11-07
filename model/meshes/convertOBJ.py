import os
import sys
import vtk


def writePolyData(polyData, outFile):

    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName(outFile)
    writer.SetInput(polyData)
    writer.Write()


def createPolyData(faces, vtList, verts, tcoords, normals):

    points = vtk.vtkPoints()
    points.SetDataTypeToDouble()
    points.SetNumberOfPoints(len(vtList))

    tcoordArray = vtk.vtkDoubleArray()
    tcoordArray.SetName('tcoords')
    tcoordArray.SetNumberOfComponents(2)
    tcoordArray.SetNumberOfTuples(len(vtList))

    normalsArray = vtk.vtkDoubleArray()
    normalsArray.SetName('normals')
    normalsArray.SetNumberOfComponents(3)
    normalsArray.SetNumberOfTuples(len(vtList))

    for i, vt in enumerate(vtList):
        vi, ti, ni = vt
        xyz = verts[vi]
        uv = tcoords[ti]
        normal = normals[ni]

        points.SetPoint(i, xyz)
        tcoordArray.SetTuple2(i, uv[0], uv[1])
        normalsArray.SetTuple3(i, normal[0], normal[1], normal[2])

    cells = vtk.vtkCellArray()

    for i, face in enumerate(faces):
        tri = vtk.vtkTriangle()
        tri.GetPointIds().SetId(0, face[0])
        tri.GetPointIds().SetId(1, face[1])
        tri.GetPointIds().SetId(2, face[2])
        cells.InsertNextCell(tri)

    polyData = vtk.vtkPolyData()
    polyData.SetPoints(points)
    polyData.SetPolys(cells)
    polyData.GetPointData().SetTCoords(tcoordArray)
    polyData.GetPointData().SetNormals(normalsArray)
    return polyData


def readObj(inFile):

    f = open(inFile)

    verts = []
    normals = []
    tcoords = []
    faces = []

    vtList = []
    vtMap = {}

    for line in f:

        line = line.strip()
        if not line or line.startswith("#"):
            continue

        fields = line.split()
        entry = fields[0]

        if entry == 'v':
            verts.append([float(x) for x in fields[1:]])
        elif entry == 'vn':
            normals.append([float(x) for x in fields[1:]])
        elif entry == 'vt':
            tcoords.append([float(x) for x in fields[1:]])
        elif entry == 'f':

            face = []
            for faceTuple in fields[1:]:

                # skip faces that dont have tcoords
                if '//' in faceTuple:
                    continue

                # split "vi/ti/ni" into list of ints
                vt = [int(x)-1 for x in faceTuple.split('/')]
                vt = (vt[0], vt[1], vt[2])

                assert(vt[0] < len(verts))
                assert(vt[1] < len(tcoords))
                assert(vt[2] < len(normals))

                vtId = vtMap.get(vt)
                if not vtId:
                    vtList.append(vt)
                    vtId = len(vtList)-1
                    vtMap[vt] = vtId

                face.append(vtId)

            if face:
                # assume all faces are triangles
                assert(len(face) == 3)
                faces.append(face)

        elif entry == 'usemtl':
            pass
        elif entry == 'mtllib':
            pass
        else:
            pass

    return faces, vtList, verts, tcoords, normals


def addTextureFileMetaData(polyData, textureFile):

    s = vtk.vtkStringArray()
    s.InsertNextValue(textureFile)
    s.SetName('texture_filename')
    polyData.GetFieldData().AddArray(s)


def objToPolyData(inFile, textureFile, outFile):

    print 'reading:', inFile
    faces, vtList, verts, tcoords, normals = readObj(inFile)

    print 'face count:', len(faces)
    print 'vertex count:', len(vtList)

    polyData = createPolyData(faces, vtList, verts, tcoords, normals)

    addTextureFileMetaData(polyData, textureFile)

    print 'writing:', outFile
    writePolyData(polyData, outFile)


if __name__ == '__main__':

    if not len(sys.argv) == 3:
        print 'Usage: %s <obj file> <texture filename>' % sys.argv[0]
        sys.exit(1)

    inFile = sys.argv[1]
    outFile = os.path.splitext(inFile)[0] + '.vtp'
    textureFile = sys.argv[2]
    objToPolyData(inFile, textureFile, outFile)
