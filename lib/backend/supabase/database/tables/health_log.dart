import '../database.dart';

class HealthLogTable extends SupabaseTable<HealthLogRow> {
  @override
  String get tableName => 'health_log';

  @override
  HealthLogRow createRow(Map<String, dynamic> data) => HealthLogRow(data);
}

class HealthLogRow extends SupabaseDataRow {
  HealthLogRow(Map<String, dynamic> data) : super(data);

  @override
  SupabaseTable get table => HealthLogTable();

  String get id => getField<String>('id')!;
  set id(String value) => setField<String>('id', value);

  String get userId => getField<String>('user_id')!;
  set userId(String value) => setField<String>('user_id', value);

  String get plantId => getField<String>('plant_id')!;
  set plantId(String value) => setField<String>('plant_id', value);

  String? get detectedDisease => getField<String>('detected_disease');
  set detectedDisease(String? value) =>
      setField<String>('detected_disease', value);

  String? get treatment => getField<String>('treatment');
  set treatment(String? value) => setField<String>('treatment', value);

  DateTime? get createdAt => getField<DateTime>('created_at');
  set createdAt(DateTime? value) => setField<DateTime>('created_at', value);
}
