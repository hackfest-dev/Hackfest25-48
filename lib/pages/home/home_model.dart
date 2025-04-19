import '/components/bottomnav_widget.dart';
import '/components/topnavi_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'home_widget.dart' show HomeWidget;
import 'package:flutter/material.dart';

class HomeModel extends FlutterFlowModel<HomeWidget> {
  ///  State fields for stateful widgets in this page.

  // Model for bottomnav component.
  late BottomnavModel bottomnavModel;
  // Model for topnavi component.
  late TopnaviModel topnaviModel;

  @override
  void initState(BuildContext context) {
    bottomnavModel = createModel(context, () => BottomnavModel());
    topnaviModel = createModel(context, () => TopnaviModel());
  }

  @override
  void dispose() {
    bottomnavModel.dispose();
    topnaviModel.dispose();
  }
}
