rule _FSG_v1_33_wfpeaq
{
	meta:
		description = "FSG v1_33"
	strings:
		$a = {BEA4014000AD93AD97AD5696B280A4B680FF1373F933C9FF13731633C0FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
