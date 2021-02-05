rule _EncryptPE_V2_2006_1_15__WFS_dyzlad
{
	meta:
		description = "EncryptPE V2_2006_1_15 __ WFS"
	strings:
		$a = {609C64FF3500000000E873010000000000000000000000000000????????????????0000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
