import '../database.dart';

class NotificationTable extends SupabaseTable<NotificationRow> {
  @override
  String get tableName => 'notification';

  @override
  NotificationRow createRow(Map<String, dynamic> data) => NotificationRow(data);
}

class NotificationRow extends SupabaseDataRow {
  NotificationRow(Map<String, dynamic> data) : super(data);

  @override
  SupabaseTable get table => NotificationTable();

  String get id => getField<String>('id')!;
  set id(String value) => setField<String>('id', value);

  String get plantId => getField<String>('plant_id')!;
  set plantId(String value) => setField<String>('plant_id', value);

  String get userId => getField<String>('user_id')!;
  set userId(String value) => setField<String>('user_id', value);

  DateTime? get time => getField<DateTime>('time');
  set time(DateTime? value) => setField<DateTime>('time', value);

  String? get notificationText => getField<String>('notification_text');
  set notificationText(String? value) =>
      setField<String>('notification_text', value);
}
