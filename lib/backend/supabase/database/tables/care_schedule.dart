import '../database.dart';

class CareScheduleTable extends SupabaseTable<CareScheduleRow> {
  @override
  String get tableName => 'care_schedule';

  @override
  CareScheduleRow createRow(Map<String, dynamic> data) => CareScheduleRow(data);
}

class CareScheduleRow extends SupabaseDataRow {
  CareScheduleRow(Map<String, dynamic> data) : super(data);

  @override
  SupabaseTable get table => CareScheduleTable();

  String get id => getField<String>('id')!;
  set id(String value) => setField<String>('id', value);

  String get plantId => getField<String>('plant_id')!;
  set plantId(String value) => setField<String>('plant_id', value);

  String get userId => getField<String>('user_id')!;
  set userId(String value) => setField<String>('user_id', value);

  DateTime get date => getField<DateTime>('date')!;
  set date(DateTime value) => setField<DateTime>('date', value);

  String? get day => getField<String>('day');
  set day(String? value) => setField<String>('day', value);

  String? get task => getField<String>('task');
  set task(String? value) => setField<String>('task', value);

  String? get reason => getField<String>('reason');
  set reason(String? value) => setField<String>('reason', value);

  String? get notificationId => getField<String>('notification_id');
  set notificationId(String? value) =>
      setField<String>('notification_id', value);

  DateTime? get createdAt => getField<DateTime>('created_at');
  set createdAt(DateTime? value) => setField<DateTime>('created_at', value);
}
