import '../database.dart';

class GrowthAnalysisTable extends SupabaseTable<GrowthAnalysisRow> {
  @override
  String get tableName => 'growth_analysis';

  @override
  GrowthAnalysisRow createRow(Map<String, dynamic> data) =>
      GrowthAnalysisRow(data);
}

class GrowthAnalysisRow extends SupabaseDataRow {
  GrowthAnalysisRow(Map<String, dynamic> data) : super(data);

  @override
  SupabaseTable get table => GrowthAnalysisTable();

  String get id => getField<String>('id')!;
  set id(String value) => setField<String>('id', value);

  String get plantId => getField<String>('plant_id')!;
  set plantId(String value) => setField<String>('plant_id', value);

  String get userId => getField<String>('user_id')!;
  set userId(String value) => setField<String>('user_id', value);

  String? get imageUrl => getField<String>('image_url');
  set imageUrl(String? value) => setField<String>('image_url', value);

  double? get growthScore => getField<double>('growth_score');
  set growthScore(double? value) => setField<double>('growth_score', value);

  dynamic get deltaMetrics => getField<dynamic>('delta_metrics');
  set deltaMetrics(dynamic value) => setField<dynamic>('delta_metrics', value);

  DateTime? get createdAt => getField<DateTime>('created_at');
  set createdAt(DateTime? value) => setField<DateTime>('created_at', value);
}
