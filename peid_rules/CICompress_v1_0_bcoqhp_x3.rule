rule _CICompress_v1_0_bcoqhp
{
	meta:
		description = "CICompress v1_0"
	strings:
		$a = {535152565755E8000000005D8BD581EDA23040002B959133400081EA0B00000089959A33400080BD993340000074}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
