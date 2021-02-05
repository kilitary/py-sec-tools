rule _PRO_PACK_v2_08_xdkxnv
{
	meta:
		description = "PRO_PACK v2_08"
	strings:
		$a = {83EC??8BECBE????FCE8????05????8BC8E8????8B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
