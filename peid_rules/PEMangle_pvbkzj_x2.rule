rule _PEMangle_pvbkzj
{
	meta:
		description = "PEMangle"
	strings:
		$a = {609CBE001040008BFEB928030000BB78563412AD33C3ABE2FA9D61}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
