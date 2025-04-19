import '/backend/api_requests/api_calls.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'update_plant_widget.dart' show UpdatePlantWidget;
import 'package:flutter/material.dart';

class UpdatePlantModel extends FlutterFlowModel<UpdatePlantWidget> {
  ///  State fields for stateful widgets in this component.

  bool isDataUploading = false;
  FFUploadedFile uploadedLocalFile =
      FFUploadedFile(bytes: Uint8List.fromList([]));

  // Stores action output result for [Custom Action - convertImageToBase64] action in Button widget.
  String? imageInBase64;
  // Stores action output result for [Backend Call - API (healthcheck)] action in Button widget.
  ApiCallResponse? apiResult;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {}
}
