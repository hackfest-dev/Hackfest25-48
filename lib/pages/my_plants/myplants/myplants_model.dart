import '/components/topnavbar_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'myplants_widget.dart' show MyplantsWidget;
import 'package:flutter/material.dart';

class MyplantsModel extends FlutterFlowModel<MyplantsWidget> {
  ///  State fields for stateful widgets in this page.

  // Model for topnavbar component.
  late TopnavbarModel topnavbarModel;

  @override
  void initState(BuildContext context) {
    topnavbarModel = createModel(context, () => TopnavbarModel());
  }

  @override
  void dispose() {
    topnavbarModel.dispose();
  }
}
