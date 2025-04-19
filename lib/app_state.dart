import 'package:flutter/material.dart';

class FFAppState extends ChangeNotifier {
  static FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal();

  static void reset() {
    _instance = FFAppState._internal();
  }

  Future initializePersistedState() async {}

  void update(VoidCallback callback) {
    callback();
    notifyListeners();
  }

  String _imageField = '';
  String get imageField => _imageField;
  set imageField(String value) {
    _imageField = value;
  }

  String _nameFiled = '';
  String get nameFiled => _nameFiled;
  set nameFiled(String value) {
    _nameFiled = value;
  }
}
