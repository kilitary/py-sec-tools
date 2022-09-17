rule _PE_Packer_fejsnt
{
	meta:
		description = "PE Packer"
	strings:
		$a = {FC8B35700140??83EE406A4068??3010}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
