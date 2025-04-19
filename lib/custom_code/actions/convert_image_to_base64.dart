// Automatic FlutterFlow imports
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'index.dart'; // Imports other custom actions
import 'package:flutter/material.dart';
// Begin custom action code
// DO NOT REMOVE OR MODIFY THE CODE ABOVE!

import 'dart:convert';
import 'dart:io';
import 'package:flutter/services.dart';

Future<String> convertImageToBase64(String filePath) async {
  final File imageFile = File(filePath);
  final List<int> imageBytes = await imageFile.readAsBytes();
  final String base64Image = base64Encode(imageBytes);
  return base64Image;
}
