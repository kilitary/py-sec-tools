rule _FSG_v1_3_sqbgpx
{
	meta:
		description = "FSG v1_3"
	strings:
		$a = {BEA4014000AD93AD97AD5696B280A4B680FF1373}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
