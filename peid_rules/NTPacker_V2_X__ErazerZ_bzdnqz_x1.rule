rule _NTPacker_V2_X__ErazerZ_bzdnqz
{
	meta:
		description = "NTPacker V2_X __ ErazerZ"
	strings:
		$a = {4B57696E646F7773001055547970657300003F756E744D61696E46756E6374696F6E73000047756E744279706173730000B761504C696275000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
