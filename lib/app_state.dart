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

  /// Stored Longitude value for device's current position
  double _VarLong = 0.0;
  double get VarLong => _VarLong;
  set VarLong(double value) {
    _VarLong = value;
  }

  /// Stored Latitude value for device's current position
  double _VarLati = 0.0;
  double get VarLati => _VarLati;
  set VarLati(double value) {
    _VarLati = value;
  }
}
