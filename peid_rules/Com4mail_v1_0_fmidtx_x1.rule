rule _Com4mail_v1_0_fmidtx
{
	meta:
		description = "Com4mail v1_0"
	strings:
		$a = {424547494E3D3D3D74667564236F665F436F6D344D61696C5F66696C65230D0A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
