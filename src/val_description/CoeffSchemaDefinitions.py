schema_header = '''
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
'''

actuator_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
    <xs:restriction base="xs:string">
        <xs:enumeration value="AltVel_MountingGain"/>
        <xs:enumeration value="EncMountingDir"/>
        <xs:enumeration value="EncoderIndexOffset"/>
        <xs:enumeration value="JointKinematicDir"/>
        <xs:enumeration value="JointOutputAPS_MountingGain"/>
        <xs:enumeration value="JointSensors_MotorPosition"/>
        <xs:enumeration value="JointSensors_OutputForce"/>
        <xs:enumeration value="JointSensors_OutputPosition"/>
        <xs:enumeration value="JointSensors_OutputVelocity"/>
        <xs:enumeration value="JointSensors_LinearPosition"/>
        <xs:enumeration value="JointSensors_LinearVelocity"/>
        <xs:enumeration value="PositionOffset_Rad"/>
        <xs:enumeration value="SpringAPS_BitOffset"/>
        <xs:enumeration value="SpringAPS_MountingGain"/>
        <xs:enumeration value="LoadCell_MountingGain"/>
        <xs:enumeration value="LoadCell_OffsetBits"/>
        <xs:enumeration value="LoadCell_NmPerCount"/>
        <xs:enumeration value="TemperatureSensor_SensorLoc1"/>
        <xs:enumeration value="TemperatureSensor_SensorLoc2"/>
        <xs:enumeration value="TorqueOffset_Nm"/>
        <xs:enumeration value="ForceOffset_N"/>
    </xs:restriction>
</xs:simpleType>
'''

athena1_actuator_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
    <xs:restriction base="xs:string">
        <xs:enumeration value="Pitch_offset"/>
        <xs:enumeration value="Yaw_offset"/>
        <xs:enumeration value="Pitch_hilmt"/>
        <xs:enumeration value="Pitch_lolmt"/>
        <xs:enumeration value="Pitch_cnvtrad"/>
        <xs:enumeration value="Yaw_hilmt"/>
        <xs:enumeration value="Yaw_lolmt"/>
        <xs:enumeration value="Yaw_cnvtrad"/>
        <xs:enumeration value="thumb_hicmdlmt"/>
        <xs:enumeration value="thumb_locmdlmt"/>
        <xs:enumeration value="thumb_posKP"/>
        <xs:enumeration value="thumb_posKD"/>
        <xs:enumeration value="thumb_dutylmt"/>
        <xs:enumeration value="WL_Torq_KP"/>
        <xs:enumeration value="WL_Torq_KD"/>
        <xs:enumeration value="WL_hiposcmdlmt"/>
        <xs:enumeration value="WL_loposcmdlmt"/>
        <xs:enumeration value="WL_hivelcmdlmt"/>
        <xs:enumeration value="WL_lovelcmdlmt"/>
        <xs:enumeration value="WL_posKP"/>
        <xs:enumeration value="WL_posKD"/>
        <xs:enumeration value="WL_dutylmt"/>
        <xs:enumeration value="Fing3_elecoffset"/>
        <xs:enumeration value="Fing3_locmdlmt"/>
        <xs:enumeration value="Fing3_hicmdlmt"/>
        <xs:enumeration value="Fing3_posKP"/>
        <xs:enumeration value="Fing3_posKD"/>
        <xs:enumeration value="Fing3_dutylmt"/>
        <xs:enumeration value="Fing3_APSoffset"/>
        <xs:enumeration value="WR_Torq_KP"/>
        <xs:enumeration value="WR_Torq_KD"/>
        <xs:enumeration value="WR_hiposcmdlmt"/>
        <xs:enumeration value="WR_loposcmdlmt"/>
        <xs:enumeration value="WR_hivelcmdlmt"/>
        <xs:enumeration value="WR_lovelcmdlmt"/>
        <xs:enumeration value="WR_posKP"/>
        <xs:enumeration value="WR_posKD"/>
        <xs:enumeration value="WR_dutylmt"/>
    </xs:restriction>
</xs:simpleType>
'''

athena2_actuator_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
    <xs:restriction base="xs:string">
        <xs:enumeration value="Fing1_elecoffset"/>
        <xs:enumeration value="Fing1_locmdlmt"/>
        <xs:enumeration value="Fing1_hicmdlmt"/>
        <xs:enumeration value="Fing1_posKP"/>
        <xs:enumeration value="Fing1_posKD"/>
        <xs:enumeration value="Fing1_dutylmt"/>
        <xs:enumeration value="Fing1_APSoffset"/>
        <xs:enumeration value="Fing2_elecoffset"/>
        <xs:enumeration value="Fing2_locmdlmt"/>
        <xs:enumeration value="Fing2_hicmdlmt"/>
        <xs:enumeration value="Fing2_posKP"/>
        <xs:enumeration value="Fing2_posKD"/>
        <xs:enumeration value="Fing2_dutylmt"/>
        <xs:enumeration value="Fing2_APSoffset"/>
        <xs:enumeration value="Fing3_elecoffset"/>
        <xs:enumeration value="Fing3_locmdlmt"/>
        <xs:enumeration value="Fing3_hicmdlmt"/>
        <xs:enumeration value="Fing3_posKP"/>
        <xs:enumeration value="Fing3_posKD"/>
        <xs:enumeration value="Fing3_dutylmt"/>
        <xs:enumeration value="Fing3_APSoffset"/>
        <xs:enumeration value="Fing4_elecoffset"/>
        <xs:enumeration value="Fing4_locmdlmt"/>
        <xs:enumeration value="Fing4_hicmdlmt"/>
        <xs:enumeration value="Fing4_posKP"/>
        <xs:enumeration value="Fing4_posKD"/>
        <xs:enumeration value="Fing4_dutylmt"/>
        <xs:enumeration value="Fing4_APSoffset"/>
    </xs:restriction>
</xs:simpleType>
'''

class_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
    <xs:restriction base="xs:string">
        <xs:enumeration value="JointTorqueLimit_Nm"/>
        <xs:enumeration value="JointForceLimit_N"/>
        <xs:enumeration value="CurrentSafeLimit"/>
        <xs:enumeration value="EncoderCPR"/>
        <xs:enumeration value="FluxLinkage"/>
        <xs:enumeration value="Inductance_DAxis"/>
        <xs:enumeration value="Inductance_QAxis"/>
        <xs:enumeration value="JointGearRatio"/>
        <xs:enumeration value="JointMaxValue"/>
        <xs:enumeration value="JointMinValue"/>
        <xs:enumeration value="JointOutputAPS_CountsToRad"/>
        <xs:enumeration value="JointRadToLinear"/>
        <xs:enumeration value="JointSafety_LimitZone_Rad"/>
        <xs:enumeration value="JointSafety_LimitZone_m"/>
        <xs:enumeration value="LoadCell_NPerCount"/>
        <xs:enumeration value="MotorWindingType"/>
        <xs:enumeration value="NumberOfPoles"/>
        <xs:enumeration value="Renishaw_CountsToRad"/>
        <xs:enumeration value="Renishaw_CountsToM"/>
        <xs:enumeration value="SpringStiffness"/>
        <xs:enumeration value="WindingResistance"/>
    </xs:restriction>
</xs:simpleType>
'''

controller_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
  <xs:restriction base="xs:string">
    <xs:enumeration value="Commutation_Select"/>
    <xs:enumeration value="CurrVelFilter_fc_Hz"/>
    <xs:enumeration value="DeadTimeCompensation"/>
    <xs:enumeration value="JointVelFilter_fc_Hz"/>
    <xs:enumeration value="MotorAccFilter_fc_Hz"/>
    <xs:enumeration value="MotorVelFilter_fc_Hz"/>
    <xs:enumeration value="PositionControl_Kd"/>
    <xs:enumeration value="PositionControl_Kp"/>
    <xs:enumeration value="PositionControl_SensorFeedback"/>
    <xs:enumeration value="PositionControl_MotorTorqueDirection"/>
    <xs:enumeration value="SpaceVector_CurrentToSV"/>
    <xs:enumeration value="SpaceVector_MaxNormVoltage"/>
    <xs:enumeration value="TorqueControl_Current2MotorTorque"/>
    <xs:enumeration value="TorqueControl_FFd_fc_Hz"/>
    <xs:enumeration value="TorqueControl_Kd"/>
    <xs:enumeration value="TorqueControl_Kd_fc_Hz"/>
    <xs:enumeration value="TorqueControl_Kp"/>
    <xs:enumeration value="TorqueControl_PD_damp"/>
    <xs:enumeration value="TorqueControl_ParallelDamping"/>
    <xs:enumeration value="TorqueControl_TdobWindupLimit_Nm"/>
    <xs:enumeration value="TorqueControl_Tdob_fc_Hz"/>
    <xs:enumeration value="TorqueControl_autoKd"/>
    <xs:enumeration value="TorqueControl_b"/>
    <xs:enumeration value="TorqueControl_enableDOB"/>
    <xs:enumeration value="TorqueControl_enableDynFF"/>
    <xs:enumeration value="TorqueControl_enableFF"/>
    <xs:enumeration value="TorqueControl_enablePID"/>
    <xs:enumeration value="TorqueControl_m"/>
    <xs:enumeration value="EffortControl_Alpha"/>
    <xs:enumeration value="EffortControl_AlphaDot"/>
    <xs:enumeration value="EffortControl_OnlineTuning"/>
    <xs:enumeration value="TorqueControl_MotorTorqueDirection"/>
    <xs:enumeration value="ForceControl_m"/>
    <xs:enumeration value="ForceControl_b"/>
    <xs:enumeration value="ForceControl_Current2MotorForce"/>
    <xs:enumeration value="ForceControl_enableFF"/>
    <xs:enumeration value="ForceControl_enablePID"/>
    <xs:enumeration value="ForceControl_Kp"/>
    <xs:enumeration value="ForceControl_Kd"/>
    <xs:enumeration value="ForceControl_PD_damp"/>
    <xs:enumeration value="ForceControl_autoKd"/>
    <xs:enumeration value="ForceControl_Kd_fc_Hz"/>
    <xs:enumeration value="ForceControl_dobWindupLimit_N"/>
    <xs:enumeration value="ForceControl_dob_fc_Hz"/>
    <xs:enumeration value="ForceControl_enableDOB"/>
    <xs:enumeration value="ForceControl_FFd_fc_Hz"/>
    <xs:enumeration value="ForceControl_enableDynFF"/>
    <xs:enumeration value="ForceControl_ParallelDamping"/>
    <xs:enumeration value="ForceControl_SensorFeedback"/>
    <xs:enumeration value="ForceControl_MotorForceDirection"/>
  </xs:restriction>
</xs:simpleType>
'''

location_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
  <xs:restriction base="xs:string">
    <xs:enumeration value="JointSafety_LowerLimit_Rad"/>
    <xs:enumeration value="JointSafety_UpperLimit_Rad"/>
    <xs:enumeration value="JointSafety_LowerLimit_m"/>
    <xs:enumeration value="JointSafety_UpperLimit_m"/>
  </xs:restriction>
</xs:simpleType>
'''

location_files_definition = \
    '''
  <xs:simpleType name="ValidLocations">
    <xs:restriction base="xs:string">
      <xs:enumeration value="shoulder_pitch.xml"/>
      <xs:enumeration value="hip_yaw_right.xml"/>
      <xs:enumeration value="hip_yaw_left.xml"/>
      <xs:enumeration value="torso_yaw.xml"/>
      <xs:enumeration value="hip_roll_right.xml"/>
      <xs:enumeration value="hip_roll_left.xml"/>
      <xs:enumeration value="shoulder_roll_left.xml"/>
      <xs:enumeration value="shoulder_roll_right.xml"/>
      <xs:enumeration value="hip_pitch.xml"/>
      <xs:enumeration value="knee_pitch.xml"/>
      <xs:enumeration value="trunk.xml"/>
      <xs:enumeration value="ankle.xml"/>
      <xs:enumeration value="shoulder_yaw.xml"/>
      <xs:enumeration value="elbow_pitch_left.xml"/>
      <xs:enumeration value="elbow_pitch_right.xml"/>
      <xs:enumeration value="neck_lower.xml"/>
      <xs:enumeration value="neck_upper.xml"/>
      <xs:enumeration value="neck_yaw.xml"/>
      <xs:enumeration value="forearm_yaw.xml"/>
    </xs:restriction>
  </xs:simpleType>
'''

sensor_files_definition = \
    '''
  <xs:simpleType name="ValidSensorFiles">
    <xs:restriction base="xs:string">
      <xs:enumeration value="sensors.xml"/>
      <xs:enumeration value="sensors_leonidas.xml"/>
    </xs:restriction>
  </xs:simpleType>
'''

safety_file_definitions = \
    '''
  <xs:simpleType name="ValidSafetyFiles">
    <xs:restriction base="xs:string">
      <xs:enumeration value="safety.xml"/>
    </xs:restriction>
  </xs:simpleType>
'''

safety_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
  <xs:restriction base="xs:string">
    <xs:enumeration value="APS1DriftSafeLimit"/>
    <xs:enumeration value="CommTimeoutMs"/>
    <xs:enumeration value="DeltaAPSSafeLimit"/>
    <xs:enumeration value="EncDriftSafeLimit"/>
    <xs:enumeration value="JerkSafeLimit"/>
    <xs:enumeration value="TemperatureSensor_MaxTemp1"/>
    <xs:enumeration value="TemperatureSensor_MaxTemp2"/>
    <xs:enumeration value="TemperatureSensor_SensorLoc1"/>
    <xs:enumeration value="TemperatureSensor_SensorLoc2"/>
    <xs:enumeration value="VelocitySafeLimit"/>
  </xs:restriction>
</xs:simpleType>
'''

sensor_coeffs_definition = \
    '''
<xs:simpleType name="ValidCoeffs">
  <xs:restriction base="xs:string">
    <xs:enumeration value="BusVoltage_BitOffset"/>
    <xs:enumeration value="BusVoltage_SensorGain"/>
    <xs:enumeration value="IGainAmpsPerBit"/>
    <xs:enumeration value="PhaseACurOffset"/>
    <xs:enumeration value="PhaseBCurOffset"/>
    <xs:enumeration value="PhaseCCurOffset"/>
    <xs:enumeration value="Position_Alpha"/>
    <xs:enumeration value="Velocity_Alpha"/>
  </xs:restriction>
</xs:simpleType>
'''

actuator_class_info_definition = \
    '''
<xs:element name="Type">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="Processor">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="ScheduleFile">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
'''

actuator_coeff_files_definition = \
    '''
<xs:element name="ClassFile">
      <xs:complexType>
      <xs:sequence>
            <xs:element name="SubClassFile" minOccurs="0">
                  <xs:complexType>
                      <xs:attribute name="id" type="xs:string"></xs:attribute>
                  </xs:complexType>
            </xs:element>
      </xs:sequence>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="ControllerFile">
      <xs:complexType>
      <xs:sequence>
            <xs:element name="SubControllerFile" minOccurs="0">
                  <xs:complexType>
                      <xs:attribute name="id" type="xs:string"></xs:attribute>
                  </xs:complexType>
            </xs:element>
      </xs:sequence>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="LocationFile">
      <xs:complexType>
            <xs:attribute name="id" type="ValidLocations"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="SensorsFile">
      <xs:complexType>
            <xs:attribute name="id" type="ValidSensorFiles"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="SafetyFile">
      <xs:complexType>
            <xs:attribute name="id" type="ValidSafetyFiles"></xs:attribute>
      </xs:complexType>
</xs:element>
'''

header_coeff_definition = \
    '''
    <xs:element name="CoeffData">
        <xs:complexType>
        <xs:sequence>
'''

footer_coeff_definition = \
    '''
             </xs:element>
        </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
'''

coeff_definition = \
    '''
                  <xs:element name="Coeffs">
                  <xs:complexType>
                  <xs:sequence>
                      <xs:element name="Coeff" maxOccurs="unbounded">
                            <xs:complexType>
                                  <xs:attribute name="id" type="ValidCoeffs"/>
                                  <xs:attribute name="description" type="xs:string"/>
                                  <xs:attribute name="value" type="xs:float"/>
                            </xs:complexType>
                      </xs:element>
                  </xs:sequence>
                  </xs:complexType>
'''
