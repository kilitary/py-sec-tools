rule _EncryptPE_V2_2006_7_10__WFS_quspuz
{
	meta:
		description = "EncryptPE V2_2006_7_10 __ WFS"
	strings:
		$a = {609C64FF3500000000E873010000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
