rule _FSG_v1_10_Eng___dulekxt_nmdvhz
{
	meta:
		description = "FSG v1_10 _Eng_ __ dulekxt"
	strings:
		$a = {EB01??E8??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
