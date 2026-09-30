const DESCRIPTION_LIMIT : number = 31;

export const displayDescription = (str:string|null)=>{
  const description = str ?? "";
  const isTruncated = description.length > DESCRIPTION_LIMIT;
  const displayedDescription = description.slice(0,DESCRIPTION_LIMIT);
  return isTruncated?`${displayedDescription}...`: displayedDescription
}