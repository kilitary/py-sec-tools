rule _Unknown_packer_03__imgzjd
{
	meta:
		description = "Unknown packer _03_"
	strings:
		$a = {061E575650535152BD????0E1F8C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
