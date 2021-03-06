def toMSCKF(path,
            calib_file, T_cn_cnm1,
            cam0_params, cam1_params):
  file = open(path + calib_file, 'w')

  file.write('cam0:\n')
  file.write('  T_cam_imu:\n')
  file.write('    [{: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam0_params['T_cam_imu'][0][0], cam0_params['T_cam_imu'][0][1], cam0_params['T_cam_imu'][0][2], cam0_params['T_cam_imu'][0][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam0_params['T_cam_imu'][1][0], cam0_params['T_cam_imu'][1][1], cam0_params['T_cam_imu'][1][2], cam0_params['T_cam_imu'][1][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam0_params['T_cam_imu'][2][0], cam0_params['T_cam_imu'][2][1], cam0_params['T_cam_imu'][2][2], cam0_params['T_cam_imu'][2][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e}]\n'.format(cam0_params['T_cam_imu'][3][0], cam0_params['T_cam_imu'][3][1], cam0_params['T_cam_imu'][3][2], cam0_params['T_cam_imu'][3][3]))
  file.write('  camera_model: pinhole\n')
  file.write('  distortion_coeffs: [{:.12e}, {:.12e}, {:.12e}, {:.12e}]\n'.format(cam0_params['distortion'][0], cam0_params['distortion'][1], cam0_params['distortion'][2], cam0_params['distortion'][3]))
  file.write('  distortion_model: radtan\n')
  file.write('  intrinsics: [{:.12e}, {:.12e}, {:.12e}, {:.12e}]\n'.format(cam0_params['intrinsics'][0], cam0_params['intrinsics'][1], cam0_params['intrinsics'][2], cam0_params['intrinsics'][3]))
  file.write('  resolution: [{:d}, {:d}]\n'.format(int(cam0_params['resolution'][0]), int(cam0_params['resolution'][1])))
  file.write('  timeshift_cam_imu: 0.0\n')
  file.write('cam1:\n')
  file.write('  T_cam_imu:\n')
  file.write('    [{: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam1_params['T_cam_imu'][0][0], cam1_params['T_cam_imu'][0][1], cam1_params['T_cam_imu'][0][2], cam1_params['T_cam_imu'][0][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam1_params['T_cam_imu'][1][0], cam1_params['T_cam_imu'][1][1], cam1_params['T_cam_imu'][1][2], cam1_params['T_cam_imu'][1][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(cam1_params['T_cam_imu'][2][0], cam1_params['T_cam_imu'][2][1], cam1_params['T_cam_imu'][2][2], cam1_params['T_cam_imu'][2][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e}]\n'.format(cam1_params['T_cam_imu'][3][0], cam1_params['T_cam_imu'][3][1], cam1_params['T_cam_imu'][3][2], cam1_params['T_cam_imu'][3][3]))
  file.write('  T_cn_cnm1:\n')
  file.write('    [{: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(T_cn_cnm1[0][0], T_cn_cnm1[0][1], T_cn_cnm1[0][2], T_cn_cnm1[0][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(T_cn_cnm1[1][0], T_cn_cnm1[1][1], T_cn_cnm1[1][2], T_cn_cnm1[1][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e},\n'.format(T_cn_cnm1[2][0], T_cn_cnm1[2][1], T_cn_cnm1[2][2], T_cn_cnm1[2][3]))
  file.write('     {: .12e}, {: .12e}, {: .12e}, {: .12e}]\n'.format(T_cn_cnm1[3][0], T_cn_cnm1[3][1], T_cn_cnm1[3][2], T_cn_cnm1[3][3]))
  file.write('  camera_model: pinhole\n')
  file.write('  distortion_coeffs: [{:.12e}, {:.12e}, {:.12e}, {:.12e}]\n'.format(cam1_params['distortion'][0], cam1_params['distortion'][1], cam1_params['distortion'][2], cam1_params['distortion'][3]))
  file.write('  distortion_model: radtan\n')
  file.write('  intrinsics: [{:.12e}, {:.12e}, {:.12e}, {:.12e}]\n'.format(cam1_params['intrinsics'][0], cam1_params['intrinsics'][1], cam1_params['intrinsics'][2], cam1_params['intrinsics'][3]))
  file.write('  resolution: [{:d}, {:d}]\n'.format(int(cam1_params['resolution'][0]), int(cam1_params['resolution'][1])))
  file.write('  timeshift_cam_imu: 0.0\n')
  file.write('T_imu_body:\n')
  file.write('  [1.0, 0.0, 0.0, 0.0,\n')
  file.write('   0.0, 1.0, 0.0, 0.0,\n')
  file.write('   0.0, 0.0, 1.0, 0.0,\n')
  file.write('   0.0, 0.0, 0.0, 1.0]\n')
