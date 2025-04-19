import '/components/bottomnav_widget.dart';
import '/components/topnavi_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'healthlogdetail_widget.dart' show HealthlogdetailWidget;
import 'package:flutter/material.dart';

class HealthlogdetailModel extends FlutterFlowModel<HealthlogdetailWidget> {
  ///  State fields for stateful widgets in this page.

  // Model for topnavi component.
  late TopnaviModel topnaviModel;
  // State field(s) for TabBar widget.
  TabController? tabBarController;
  int get tabBarCurrentIndex =>
      tabBarController != null ? tabBarController!.index : 0;
  int get tabBarPreviousIndex =>
      tabBarController != null ? tabBarController!.previousIndex : 0;

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
    tabBarController?.dispose();
    bottomnavModel.dispose();
  }
}
