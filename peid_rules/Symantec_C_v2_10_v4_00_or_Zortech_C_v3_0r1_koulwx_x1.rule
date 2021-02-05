rule _Symantec_C_v2_10_v4_00_or_Zortech_C_v3_0r1_koulwx
{
	meta:
		description = "Symantec C v2_10_ v4_00 or Zortech C v3_0r1"
	strings:
		$a = {FAFCB8????8ED8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
