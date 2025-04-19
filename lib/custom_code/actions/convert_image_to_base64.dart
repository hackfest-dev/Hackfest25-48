// Automatic FlutterFlow imports
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'index.dart'; // Imports other custom actions
import 'package:flutter/material.dart';
// Begin custom action code
// DO NOT REMOVE OR MODIFY THE CODE ABOVE!

import 'dart:convert';
import 'dart:io';
// import 'package:flutter_flow/flutter_flow_util.dart';

Future<String> convertImageToBase64(FFUploadedFile file) async {
  if (file.bytes != null) {
    return base64Encode(file.bytes!);
  } else {
    throw Exception("File does not contain byte data.");
  }
}
