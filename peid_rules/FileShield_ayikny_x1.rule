rule _FileShield_ayikny
{
	meta:
		description = "FileShield"
	strings:
		$a = {501EEB??9000008BD8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
