import { createElement, forwardRef, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

type HeadingLevel = 1 | 2 | 3 | 4 | 5 | 6

export interface HeadingProps extends HTMLAttributes<HTMLHeadingElement> {
  /** Heading level (1-6) */
  level?: HeadingLevel
  children?: ReactNode
}

/** Renders h1-h6 with Void heading styles */
export const Heading = forwardRef<HTMLHeadingElement, HeadingProps>(
  ({ level = 2, className, children, ...props }, ref) => {
    return createElement(
      `h${level}`,
      { ref, className, ...props },
      children,
    )
  }
)

Heading.displayName = 'Heading'

export const H1 = forwardRef<HTMLHeadingElement, Omit<HeadingProps, 'level'>>((p, r) => <Heading ref={r} level={1} {...p} />)
export const H2 = forwardRef<HTMLHeadingElement, Omit<HeadingProps, 'level'>>((p, r) => <Heading ref={r} level={2} {...p} />)
export const H3 = forwardRef<HTMLHeadingElement, Omit<HeadingProps, 'level'>>((p, r) => <Heading ref={r} level={3} {...p} />)
export const H4 = forwardRef<HTMLHeadingElement, Omit<HeadingProps, 'level'>>((p, r) => <Heading ref={r} level={4} {...p} />)
export const H5 = forwardRef<HTMLHeadingElement, Omit<HeadingProps, 'level'>>((p, r) => <Heading ref={r} level={5} {...p} />)
export const H6 = forwardRef<HTMLHeadingElement, Omit<HeadingProps, 'level'>>((p, r) => <Heading ref={r} level={6} {...p} />)
H1.displayName = 'H1'; H2.displayName = 'H2'; H3.displayName = 'H3'
H4.displayName = 'H4'; H5.displayName = 'H5'; H6.displayName = 'H6'

export interface TextProps extends HTMLAttributes<HTMLParagraphElement> {
  /** Text color */
  color?: 'default' | 'accent' | 'muted' | 'secondary'
  /** Render as span instead of p */
  as?: 'p' | 'span'
  children?: ReactNode
}

export const Text = forwardRef<HTMLParagraphElement, TextProps>(
  ({ color = 'default', as: Tag = 'p', className, children, ...props }, ref) => {
    return createElement(
      Tag,
      {
        ref,
        className: cn(
          color === 'accent' && 'void-accent',
          color === 'muted' && 'void-muted',
          color === 'secondary' && 'void-secondary',
          color === 'default' && 'void-text',
          className,
        ),
        ...props,
      },
      children,
    )
  }
)

Text.displayName = 'Text'

export interface LabelProps extends HTMLAttributes<HTMLSpanElement> {
  children?: ReactNode
}

export const Label = forwardRef<HTMLSpanElement, LabelProps>(
  ({ className, children, ...props }, ref) => (
    <span ref={ref} className={cn('void-label', className)} {...props}>{children}</span>
  )
)

Label.displayName = 'Label'

export interface CodeProps extends HTMLAttributes<HTMLElement> {
  /** Render as a code block (pre > code) */
  block?: boolean
  children?: ReactNode
}

export const Code = forwardRef<HTMLElement, CodeProps>(
  ({ block, className, children, ...props }, ref) => {
    if (block) {
      return (
        <pre className={className}>
          <code ref={ref} {...props}>{children}</code>
        </pre>
      )
    }
    return <code ref={ref} className={className} {...props}>{children}</code>
  }
)

Code.displayName = 'Code'
