rule _Unknown_packer_07__vthonj
{
	meta:
		description = "Unknown packer _07_"
	strings:
		$a = {8CC805????50B8????50B0??068CD20683}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
