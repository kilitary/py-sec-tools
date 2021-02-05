rule _AcidCrypt_qazeow
{
	meta:
		description = "AcidCrypt"
	strings:
		$a = {BE????????0238404E75FA8BC28A1832DFC0CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
