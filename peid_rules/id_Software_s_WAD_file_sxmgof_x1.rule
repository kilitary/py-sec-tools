rule _id_Software_s_WAD_file_sxmgof
{
	meta:
		description = "id Software_s WAD file"
	strings:
		$a = {505741440B00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
