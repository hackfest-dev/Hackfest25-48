import '/components/bottomnav_widget.dart';
import '/components/topnavi_widget.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'chat_widget.dart' show ChatWidget;
import 'package:flutter/material.dart';

class ChatModel extends FlutterFlowModel<ChatWidget> {
  ///  State fields for stateful widgets in this page.

  final formKey = GlobalKey<FormState>();
  // State field(s) for task widget.
  FocusNode? taskFocusNode;
  TextEditingController? taskTextController;
  String? Function(BuildContext, String?)? taskTextControllerValidator;
  // Stores action output result for [Gemini - Generate Text] action in Button widget.
  String? response;
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
    taskFocusNode?.dispose();
    taskTextController?.dispose();

    bottomnavModel.dispose();
    topnaviModel.dispose();
  }
}
