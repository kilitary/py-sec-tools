rule _AcidCrypt_zglubs
{
	meta:
		description = "AcidCrypt"
	strings:
		$a = {60B9??????00BA??????00BE??????000238404E75FA8BC28A1832DFC0CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
