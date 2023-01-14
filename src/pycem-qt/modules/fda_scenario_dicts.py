"""Dictionaries containing GUI information for FDA scenarios."""

symmetric_stripline_dict = {
    'title': 'Symmetric Stripline',
    'description': 'This scenario simulates a symmetric stripline. The signal '
    'conductor is centered in the dielectric with two PEC ground planes - one '
    'above one and below.',
    'num_inputs': 5,
    'input1_title': 'Width (W)',
    'input1_val': 0.35,
    'input1_desc': 'Enter the width of the trace in millimeters.',
    'input2_title': 'Height (H)',
    'input2_val': 0.9,
    'input2_desc': 'Enter the height of the substrate in millimeters.',
    'input3_title': 'Trace Thickness (T)',
    'input3_val': 0.025,
    'input3_desc': 'Enter the thickness of the trace in millimeters. This is '
    'also the size of the grid cell in the Y-direction.',
    'input4_title': 'Dielectric Constant (Er)',
    'input4_val': 4,
    'input4_desc': 'Enter the dielectric constant of the substrate material.',
    'input5_title': 'X-direction grid cell size (dx)',
    'input5_val': 0.025,
    'input5_desc': 'Enter size of the grid cell in the X-direction '
    '(horizontal).',
    'num_table_rows': 1,
    'diagram': u":/fda/img/fda/diagrams/SymmetricStripline.png",
}

microstrip_dict = {
    'title': 'Microstrip',
    'description': 'This scenario simulates a microstrip transmission line. '
    'The signal conductor rests on top of a substrate. The ground plane is on '
    'the bottom of the substrate. The region above the substrate is air.',
    'num_inputs': 5,
    'input1_title': 'Width (W)',
    'input1_val': 1.9,
    'input1_desc': 'Enter the width of the trace in millimeters.',
    'input2_title': 'Height (H)',
    'input2_val': 1,
    'input2_desc': 'Enter the height of the substrate in millimeters.',
    'input3_title': 'Trace Thickness (T)',
    'input3_val': 0.1,
    'input3_desc': 'Enter the thickness of the trace in millimeters. This is '
    'also the size of the grid cell in the Y-direction.',
    'input4_title': 'Dielectric Constant (Er)',
    'input4_val': 4.4,
    'input4_desc': 'Enter the dielectric constant of the substrate material.',
    'input5_title': 'X-direction grid cell size (dx)',
    'input5_val': 0.1,
    'input5_desc': 'Enter size of the grid cell in the X-direction '
    '(horizontal).',
    'num_table_rows': 1,
    'diagram': u":/fda/img/fda/diagrams/Microstrip.png",
}


coaxial_dict = {
    'title': 'Coaxial',
    'description': 'This scenario simulates a coaxial transmission line. '
    'The center conductor is encased in a dielectric and surrounded by the '
    'outer conductor. The default dimensions are based on an SMA female '
    'connector with a Teflon dielectric.',
    'num_inputs': 5,
    'input1_title': 'Inner Diameter (Di)',
    'input1_val': 1.3,
    'input1_desc': 'Enter the diameter of the inner conductor in millimeters.',
    'input2_title': 'Outer Diameter (Do)',
    'input2_val': 4.6,
    'input2_desc': 'Enter the diameter of the outer conductor in millimeters.',
    'input3_title': 'Y-direction grid cell size (dy)',
    'input3_val': 0.05,
    'input3_desc': 'Enter size of the grid cell in the Y-direction (vertical).',
    'input4_title': 'Dielectric Constant (Er)',
    'input4_val': 2.2,
    'input4_desc': 'Enter the dielectric constant of the insulator material.',
    'input5_title': 'X-direction grid cell size (dx)',
    'input5_val': 0.1,
    'input5_desc': 'Enter size of the grid cell in the X-direction '
    '(horizontal).',
    'num_table_rows': 1,
    'diagram': u":/fda/img/fda/diagrams/Coaxial.png",
}


asymmetric_stripline_dict = {
    'title': 'Asymmetric Stripline',
    'description': 'This scenario simulates asymmetric stripline. The signal '
    'conductor is closer to the top ground plane than the bottom ground plane.',
    'num_inputs': 6,
    'input1_title': 'Width (W)',
    'input1_val': 0.35,
    'input1_desc': 'Enter the width of the trace in millimeters.',
    'input2_title': 'Height (H)',
    'input2_val': 0.9,
    'input2_desc': 'Enter the height of the substrate in millimeters.',
    'input3_title': 'Trace Thickness (T)',
    'input3_val': 0.025,
    'input3_desc': 'Enter the thickness of the trace in millimeters. This is '
    'also the size of the grid cell in the Y-direction.',
    'input4_title': 'Dielectric Constant (Er)',
    'input4_val': 4,
    'input4_desc': 'Enter the dielectric constant of the substrate material.',
    'input5_title': 'X-direction grid cell size (dx)',
    'input5_val': 0.025,
    'input5_desc': 'Enter size of the grid cell in the X-direction '
    '(horizontal).',
    'input6_title': 'Trace Offset',
    'input6_val': 0.2,
    'input6_desc': 'Enter the offset of the trace from the top ground plane '
    'in millimeters.',
    'num_table_rows': 1,
    'diagram': u":/fda/img/fda/diagrams/AsymmetricStripline.png",
}


diff_microstrip_dict = {
    'title': 'Differential Microstrip',
    'description': 'This scenario simulates a microstrip differential pair. '
    'The differential impedance is calculated by applying +/- 0.5V to the two '
    'conductors. The common impedance is calculated by applying a common 1V '
    'voltage to the two conductors.',
    'num_inputs': 6,
    'input1_title': 'Width (W)',
    'input1_val': 1.9,
    'input1_desc': 'Enter the width of the trace in millimeters.',
    'input2_title': 'Height (H)',
    'input2_val': 1,
    'input2_desc': 'Enter the height of the substrate in millimeters.',
    'input3_title': 'Trace Thickness (T)',
    'input3_val': 0.1,
    'input3_desc': 'Enter the thickness of the trace in millimeters. This is '
    'also the size of the grid cell in the Y-direction.',
    'input4_title': 'Dielectric Constant (Er)',
    'input4_val': 4.4,
    'input4_desc': 'Enter the dielectric constant of the substrate material.',
    'input5_title': 'X-direction grid cell size (dx)',
    'input5_val': 0.1,
    'input5_desc': 'Enter size of the grid cell in the X-direction '
    '(horizontal).',
    'input6_title': 'Spacing (S)',
    'input6_val': 0.2,
    'input6_desc': 'Enter the spacing between the two traces in millimeters.',
    'num_table_rows': 2,
    'diagram': u":/fda/img/fda/diagrams/DifferentialMicrostrip.png",
}

broadside_stripline_dict = {
    'title': 'Broadside Stripline',
    'description': 'This scenario simulates broadside-coupled differential '
    'stripline. A +0.5V voltage is applied to the top stripline, and a -0.5V '
    'voltage is applied to the bottom stripline.',
    'num_inputs': 6,
    'input1_title': 'Width (W)',
    'input1_val': 0.35,
    'input1_desc': 'Enter the width of the trace in millimeters.',
    'input2_title': 'Height (H)',
    'input2_val': 0.9,
    'input2_desc': 'Enter the height of the substrate in millimeters.',
    'input3_title': 'Trace Thickness (T)',
    'input3_val': 0.025,
    'input3_desc': 'Enter the thickness of the trace in millimeters. This is '
    'also the size of the grid cell in the Y-direction.',
    'input4_title': 'Dielectric Constant (Er)',
    'input4_val': 4,
    'input4_desc': 'Enter the dielectric constant of the substrate material.',
    'input5_title': 'X-direction grid cell size (dx)',
    'input5_val': 0.025,
    'input5_desc': 'Enter size of the grid cell in the X-direction '
    '(horizontal).',
    'input6_title': 'Spacing (S)',
    'input6_val': 0.2,
    'input6_desc': 'Enter the spacing between the two traces in millimeters.',
    'num_table_rows': 2,
    'diagram': u":/fda/img/fda/diagrams/BroadsideStripline.png",
}

diff_stripline_dict = {
    'title': 'Differential Stripline',
    'description': 'This scenario simulates edge-coupled differential '
    'stripline. The differential impedance is calculated by applying +/- 0.5V '
    'to the two conductors. The common impedance is calculated by applying a '
    'common 1V voltage to the two conductors.',
    'num_inputs': 6,
    'input1_title': 'Width (W)',
    'input1_val': 0.35,
    'input1_desc': 'Enter the width of the trace in millimeters.',
    'input2_title': 'Height (H)',
    'input2_val': 0.9,
    'input2_desc': 'Enter the height of the substrate in millimeters.',
    'input3_title': 'Trace Thickness (T)',
    'input3_val': 0.025,
    'input3_desc': 'Enter the thickness of the trace in millimeters. This is '
    'also the size of the grid cell in the Y-direction.',
    'input4_title': 'Dielectric Constant (Er)',
    'input4_val': 4,
    'input4_desc': 'Enter the dielectric constant of the substrate material.',
    'input5_title': 'X-direction grid cell size (dx)',
    'input5_val': 0.025,
    'input5_desc': 'Enter size of the grid cell in the X-direction '
    '(horizontal).',
    'input6_title': 'Spacing (S)',
    'input6_val': 0.2,
    'input6_desc': 'Enter the spacing between the two traces in millimeters.',
    'num_table_rows': 2,
    'diagram': u":/fda/img/fda/diagrams/DifferentialStripline.png",
}

fda_scenarios_list = [symmetric_stripline_dict,
                      microstrip_dict,
                      coaxial_dict,
                      asymmetric_stripline_dict,
                      diff_microstrip_dict,
                      broadside_stripline_dict,
                      diff_stripline_dict
                      ]
