rule _EncryptPE_1_2003_5_18__WFS_ixzrcg
{
	meta:
		description = "EncryptPE 1_2003_5_18 __ WFS"
	strings:
		$a = {555756525153E8000000005D8BD581ED973B4000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
