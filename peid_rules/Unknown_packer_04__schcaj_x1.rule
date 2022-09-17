rule _Unknown_packer_04__schcaj
{
	meta:
		description = "Unknown packer _04_"
	strings:
		$a = {BC????C32EFF2E????CF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
