rule _Krypton_v0_2_ydesag
{
	meta:
		description = "Krypton v0_2"
	strings:
		$a = {8B0C24E90A7C01??AD4240BDBE9D7A04}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
