import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/index.dart';
import 'package:badges/badges.dart' as badges;
import 'package:flutter/material.dart';
import 'topnavi_model.dart';
export 'topnavi_model.dart';

/// create a top navbar component where the there is the image of the company
/// in the top, along with the name beside it, make it so that there is also a
/// notification bell at the right side of the bar and a back button that is
/// only visible in all pages except the homepage
class TopnaviWidget extends StatefulWidget {
  const TopnaviWidget({super.key});

  @override
  State<TopnaviWidget> createState() => _TopnaviWidgetState();
}

class _TopnaviWidgetState extends State<TopnaviWidget> {
  late TopnaviModel _model;

  @override
  void setState(VoidCallback callback) {
    super.setState(callback);
    _model.onUpdate();
  }

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => TopnaviModel());

    WidgetsBinding.instance.addPostFrameCallback((_) => safeSetState(() {}));
  }

  @override
  void dispose() {
    _model.maybeDispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: FlutterFlowTheme.of(context).secondaryBackground,
        boxShadow: [
          BoxShadow(
            blurRadius: 3.0,
            color: Color(0x33000000),
            offset: Offset(
              0.0,
              1.0,
            ),
            spreadRadius: 0.0,
          )
        ],
      ),
      child: Padding(
        padding: EdgeInsetsDirectional.fromSTEB(16.0, 16.0, 16.0, 16.0),
        child: Row(
          mainAxisSize: MainAxisSize.max,
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Row(
              mainAxisSize: MainAxisSize.max,
              children: [
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(0.0, 0.0, 50.0, 0.0),
                  child: FlutterFlowIconButton(
                    borderColor: Colors.transparent,
                    borderRadius: 8.0,
                    borderWidth: 1.0,
                    buttonSize: 40.0,
                    icon: Icon(
                      Icons.arrow_back_rounded,
                      color: FlutterFlowTheme.of(context).primaryText,
                      size: 24.0,
                    ),
                    onPressed: () async {
                      context.pushNamed(Home3Widget.routeName);
                    },
                  ),
                ),
                Container(
                  decoration: BoxDecoration(),
                  child: Row(
                    mainAxisSize: MainAxisSize.max,
                    children: [
                      ClipRRect(
                        borderRadius: BorderRadius.circular(8.0),
                        child: Image.asset(
                          'assets/images/logo-transparent.png',
                          width: 40.0,
                          height: 40.0,
                          fit: BoxFit.contain,
                        ),
                      ),
                      Text(
                        'Grow Pal',
                        style:
                            FlutterFlowTheme.of(context).titleMedium.override(
                                  fontFamily: 'special gothic expanded one',
                                  fontSize: 18.0,
                                  letterSpacing: 0.0,
                                  fontWeight: FontWeight.w600,
                                  useGoogleFonts: false,
                                ),
                      ),
                    ].divide(SizedBox(width: 8.0)),
                  ),
                ),
              ].divide(SizedBox(width: 12.0)),
            ),
            badges.Badge(
              badgeContent: Text(
                '1',
                style: FlutterFlowTheme.of(context).titleSmall.override(
                      fontFamily: 'Inter Tight',
                      color: Colors.white,
                      fontSize: 10.0,
                      letterSpacing: 0.0,
                    ),
              ),
              showBadge: true,
              shape: badges.BadgeShape.circle,
              badgeColor: FlutterFlowTheme.of(context).success,
              elevation: 4.0,
              padding: EdgeInsetsDirectional.fromSTEB(8.0, 8.0, 8.0, 8.0),
              position: badges.BadgePosition.topEnd(),
              animationType: badges.BadgeAnimationType.scale,
              toAnimate: true,
              child: FlutterFlowIconButton(
                borderColor: Colors.transparent,
                borderRadius: 8.0,
                borderWidth: 1.0,
                buttonSize: 40.0,
                icon: Icon(
                  Icons.notifications_none_rounded,
                  color: FlutterFlowTheme.of(context).primaryText,
                  size: 24.0,
                ),
                onPressed: () async {
                  context.pushNamed(NotificationWidget.routeName);
                },
              ),
            ),
          ].divide(SizedBox(width: 8.0)),
        ),
      ),
    );
  }
}
