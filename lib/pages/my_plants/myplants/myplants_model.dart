import '/components/bottomnav_widget.dart';
import '/components/topnavi_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'myplants_widget.dart' show MyplantsWidget;
import 'package:flutter/material.dart';

class MyplantsModel extends FlutterFlowModel<MyplantsWidget> {
  ///  State fields for stateful widgets in this page.

  // Model for topnavi component.
  late TopnaviModel topnaviModel;
  // Model for bottomnav component.
  late BottomnavModel bottomnavModel;

  @override
  void initState(BuildContext context) {
    topnaviModel = createModel(context, () => TopnaviModel());
    bottomnavModel = createModel(context, () => BottomnavModel());
  }

  @override
  void dispose() {
    topnaviModel.dispose();
    bottomnavModel.dispose();
  }
}
