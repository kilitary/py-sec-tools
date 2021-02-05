rule _Shegerd_Dongle_V4_78__MS_Co__zyludn
{
	meta:
		description = "Shegerd Dongle V4_78 __ MS_Co_"
	strings:
		$a = {E832000000B8????????8B18C1CB0589DA368B4C240C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
