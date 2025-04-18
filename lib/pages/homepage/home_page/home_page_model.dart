import '/components/topnavi_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'home_page_widget.dart' show HomePageWidget;
import 'package:flutter/material.dart';

class HomePageModel extends FlutterFlowModel<HomePageWidget> {
  ///  State fields for stateful widgets in this page.

  // Model for topnavi component.
  late TopnaviModel topnaviModel;

  @override
  void initState(BuildContext context) {
    topnaviModel = createModel(context, () => TopnaviModel());
  }

  @override
  void dispose() {
    topnaviModel.dispose();
  }
}
