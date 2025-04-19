import '/components/bottomnav_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'notification_widget.dart' show NotificationWidget;
import 'package:flutter/material.dart';

class NotificationModel extends FlutterFlowModel<NotificationWidget> {
  ///  State fields for stateful widgets in this page.

  // Model for bottomnav component.
  late BottomnavModel bottomnavModel;

  @override
  void initState(BuildContext context) {
    bottomnavModel = createModel(context, () => BottomnavModel());
  }

  @override
  void dispose() {
    bottomnavModel.dispose();
  }
}
