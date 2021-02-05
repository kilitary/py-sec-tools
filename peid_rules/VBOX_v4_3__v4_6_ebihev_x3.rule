rule _VBOX_v4_3__v4_6_ebihev
{
	meta:
		description = "VBOX v4_3 _ v4_6"
	strings:
		$a = {8BC58BC58BC58BC58BC58BC58BC58BC58BC58BC58BC58BC58BC58BC58BC58BC5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
