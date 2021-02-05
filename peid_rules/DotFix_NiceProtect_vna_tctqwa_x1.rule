rule _DotFix_NiceProtect_vna_tctqwa
{
	meta:
		description = "DotFix NiceProtect vna"
	strings:
		$a = {60E8550000008DBD0010400068??????00033C248BF79068311040009BDBE355DB04248BC7DB442404DEC1DB1C248B1C2466AD51DB04249090DA8D77104000DB1C24D1E129}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
