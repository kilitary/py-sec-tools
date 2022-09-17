rule _EncryptPE_2_2004_8_10__2_2005_3_14__WFS_wcqxle
{
	meta:
		description = "EncryptPE 2_2004_8_10 _ 2_2005_3_14 __ WFS"
	strings:
		$a = {609C64FF3500000000E87A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
