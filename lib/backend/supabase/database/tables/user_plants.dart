import '../database.dart';

class UserPlantsTable extends SupabaseTable<UserPlantsRow> {
  @override
  String get tableName => 'user_plants';

  @override
  UserPlantsRow createRow(Map<String, dynamic> data) => UserPlantsRow(data);
}

class UserPlantsRow extends SupabaseDataRow {
  UserPlantsRow(Map<String, dynamic> data) : super(data);

  @override
  SupabaseTable get table => UserPlantsTable();

  String get id => getField<String>('id')!;
  set id(String value) => setField<String>('id', value);

  String get userId => getField<String>('user_id')!;
  set userId(String value) => setField<String>('user_id', value);

  String? get plantName => getField<String>('plant_name');
  set plantName(String? value) => setField<String>('plant_name', value);

  String? get imageUrl => getField<String>('image_url');
  set imageUrl(String? value) => setField<String>('image_url', value);

  String? get light => getField<String>('light');
  set light(String? value) => setField<String>('light', value);

  String? get soil => getField<String>('soil');
  set soil(String? value) => setField<String>('soil', value);

  String? get water => getField<String>('water');
  set water(String? value) => setField<String>('water', value);

  DateTime? get createdAt => getField<DateTime>('created_at');
  set createdAt(DateTime? value) => setField<DateTime>('created_at', value);
}
