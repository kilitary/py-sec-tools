rule _Unknown_packer_08__ixtvfo
{
	meta:
		description = "Unknown packer _08_"
	strings:
		$a = {8BC42D????24008BF857B9????BE????F3A5FDC3974F4F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
