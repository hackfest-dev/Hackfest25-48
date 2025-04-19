import '/components/bottomnav_widget.dart';
import '/components/topnavi_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/index.dart';
import 'home3_widget.dart' show Home3Widget;
import 'package:flutter/material.dart';

class Home3Model extends FlutterFlowModel<Home3Widget> {
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
