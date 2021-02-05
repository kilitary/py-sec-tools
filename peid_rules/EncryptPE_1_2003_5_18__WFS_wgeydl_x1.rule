rule _EncryptPE_1_2003_5_18__WFS_wgeydl
{
	meta:
		description = "EncryptPE 1_2003_5_18 __ WFS"
	strings:
		$a = {609C64FF3500000000E879}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
