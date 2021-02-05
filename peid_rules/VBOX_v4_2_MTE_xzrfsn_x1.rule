rule _VBOX_v4_2_MTE_xzrfsn
{
	meta:
		description = "VBOX v4_2 MTE"
	strings:
		$a = {8CE00BC58CE00BC403C5740074008BC5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
