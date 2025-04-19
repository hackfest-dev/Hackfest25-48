import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/index.dart';
import 'package:flutter/material.dart';
import 'bottomnav_model.dart';
export 'bottomnav_model.dart';

class BottomnavWidget extends StatefulWidget {
  const BottomnavWidget({
    super.key,
    int? selectedindex,
  }) : this.selectedindex = selectedindex ?? 1;

  /// the page number
  final int selectedindex;

  @override
  State<BottomnavWidget> createState() => _BottomnavWidgetState();
}

class _BottomnavWidgetState extends State<BottomnavWidget> {
  late BottomnavModel _model;

  @override
  void setState(VoidCallback callback) {
    super.setState(callback);
    _model.onUpdate();
  }

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => BottomnavModel());

    WidgetsBinding.instance.addPostFrameCallback((_) => safeSetState(() {}));
  }

  @override
  void dispose() {
    _model.maybeDispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsetsDirectional.fromSTEB(16.0, 0.0, 16.0, 16.0),
      child: Container(
        width: 360.0,
        height: 70.0,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFB39D271), Color(0xFF39D2B4)],
            stops: [0.0, 1.0],
            begin: AlignmentDirectional(0.14, -1.0),
            end: AlignmentDirectional(-0.14, 1.0),
          ),
          borderRadius: BorderRadius.only(
            bottomLeft: Radius.circular(8.0),
            bottomRight: Radius.circular(8.0),
            topLeft: Radius.circular(8.0),
            topRight: Radius.circular(8.0),
          ),
        ),
        child: Align(
          alignment: AlignmentDirectional(0.0, 0.0),
          child: Row(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Column(
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  FlutterFlowIconButton(
                    borderRadius: 8.0,
                    buttonSize: 50.0,
                    fillColor: Color(0xFF39D298),
                    icon: Icon(
                      Icons.home_outlined,
                      color: FlutterFlowTheme.of(context).info,
                      size: 24.0,
                    ),
                    onPressed: () async {
                      context.pushNamed(HomePageWidget.routeName);
                    },
                  ),
                  SizedBox(
                    width: 30.0,
                    child: Divider(
                      height: 2.0,
                      thickness: 2.0,
                      color: FlutterFlowTheme.of(context).alternate,
                    ),
                  ),
                ],
              ),
              Column(
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  FlutterFlowIconButton(
                    borderRadius: 8.0,
                    buttonSize: 50.0,
                    fillColor: Color(0xFF39D298),
                    icon: Icon(
                      Icons.turned_in_not_sharp,
                      color: FlutterFlowTheme.of(context).info,
                      size: 24.0,
                    ),
                    onPressed: () async {
                      context.pushNamed(HealthWidget.routeName);
                    },
                  ),
                  SizedBox(
                    width: 30.0,
                    child: Divider(
                      height: 2.0,
                      thickness: 2.0,
                      color: FlutterFlowTheme.of(context).alternate,
                    ),
                  ),
                ],
              ),
              Column(
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  FlutterFlowIconButton(
                    borderRadius: 8.0,
                    buttonSize: 50.0,
                    fillColor: Color(0xFF39D298),
                    icon: Icon(
                      Icons.chat_outlined,
                      color: FlutterFlowTheme.of(context).info,
                      size: 24.0,
                    ),
                    onPressed: () {
                      print('IconButton pressed ...');
                    },
                  ),
                  SizedBox(
                    width: 30.0,
                    child: Divider(
                      height: 2.0,
                      thickness: 2.0,
                      color: FlutterFlowTheme.of(context).alternate,
                    ),
                  ),
                ],
              ),
              Column(
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  if (widget.selectedindex == 4)
                    FlutterFlowIconButton(
                      borderRadius: 8.0,
                      buttonSize: 50.0,
                      fillColor: Color(0xFF39D298),
                      icon: Icon(
                        Icons.person_outline,
                        color: FlutterFlowTheme.of(context).info,
                        size: 24.0,
                      ),
                      onPressed: () async {
                        context.pushNamed(UserProfileWidget.routeName);
                      },
                    ),
                  SizedBox(
                    width: 30.0,
                    child: Divider(
                      height: 2.0,
                      thickness: 2.0,
                      color: FlutterFlowTheme.of(context).alternate,
                    ),
                  ),
                ],
              ),
            ]
                .divide(SizedBox(width: 16.0))
                .addToStart(SizedBox(width: 16.0))
                .addToEnd(SizedBox(width: 16.0)),
          ),
        ),
      ),
    );
  }
}
