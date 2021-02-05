rule _MEGALITE_v1_20a_usqfir
{
	meta:
		description = "MEGALITE v1_20a"
	strings:
		$a = {B8????BA????05????3B2D73??72??B409BA????CD21CD90}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
